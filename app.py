import time
import edgeiq
import cv2
"""
Use object detection to detect objects in the frame in realtime. The
types of objects detected can be changed by selecting different models.

To change the computer vision model, follow this guide:
https://dashboard.alwaysai.co/docs/application_development/changing_the_model.html

To change the engine and accelerator, follow this guide:
https://dashboard.alwaysai.co/docs/application_development/changing_the_engine_and_accelerator.html
"""


def save_snapshot(image, person_id):
    snap_date = time.strftime('%Y.%m.%d')
    snap_time = time.strftime('%H.%M.%S')
    filename = '{}-{}-person-{}.jpg'.format(snap_date, snap_time, person_id)
    cv2.imwrite(filename, image)


def main():
    obj_detect = edgeiq.ObjectDetection(
            "alwaysai/mobilenet_ssd")
    obj_detect.load(engine=edgeiq.Engine.DNN)
    tracker = edgeiq.CentroidTracker(deregister_frames=30)

    print("Loaded model:\n{}\n".format(obj_detect.model_id))
    print("Engine: {}".format(obj_detect.engine))
    print("Accelerator: {}\n".format(obj_detect.accelerator))
    print("Labels:\n{}\n".format(obj_detect.labels))

    fps = edgeiq.FPS()

    try:
        with edgeiq.WebcamVideoStream(cam=0) as video_stream, \
                edgeiq.Streamer() as streamer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()

            prev_tracked_people = {}
            logs = []

            # loop detection
            while True:
                frame = video_stream.read()
                results = obj_detect.detect_objects(frame, confidence_level=.5)
                people = edgeiq.filter_predictions_by_label(results.predictions, ['person'])
                tracked_people = tracker.update(people)

                people = []
                for (object_id, prediction) in tracked_people.items():
                    new_label = 'Person {}'.format(object_id)
                    prediction.label = new_label
                    people.append(prediction)

                frame = edgeiq.markup_image(
                        frame, people, colors=obj_detect.colors)

                new_entries = set(tracked_people) - set(prev_tracked_people)
                for entry in new_entries:
                    save_snapshot(frame, entry)
                    logs.append('Person {} entered'.format(entry))

                new_exits = set(prev_tracked_people) - set(tracked_people)
                for exit in new_exits:
                    logs.append('Person {} exited'.format(exit))

                prev_tracked_people = dict(tracked_people)

                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))
                text.append("Objects:")

                for prediction in people:
                    text.append("{}: {:2.2f}%".format(
                        prediction.label, prediction.confidence * 100))

                text.append('Logs:')
                text += logs

                streamer.send_data(frame, text)

                fps.update()

                if streamer.check_exit():
                    break

    finally:
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    main()
