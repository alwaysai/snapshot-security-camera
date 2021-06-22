import time
import edgeiq
import cv2


def save_snapshot(image):
    snap_date = time.strftime('%Y.%m.%d')
    snap_time = time.strftime('%H.%M.%S')
    filename = '{}-{}.jpg'.format(snap_date, snap_time)
    cv2.imwrite(filename, image)


def main():
    obj_detect = edgeiq.ObjectDetection("alwaysai/mobilenet_ssd")
    obj_detect.load(engine=edgeiq.Engine.DNN)

    new_detection = False

    def person_enters(person_id, prediction):
        print('Person {} enters'.format(person_id))
        nonlocal new_detection
        new_detection = True

    def person_exits(person_id, prediction):
        print('Person {} exits'.format(person_id))

    tracker = edgeiq.CentroidTracker(
            deregister_frames=30, enter_cb=person_enters, exit_cb=person_exits)

    print("Engine: {}".format(obj_detect.engine))
    print("Accelerator: {}\n".format(obj_detect.accelerator))
    print("Model:\n{}\n".format(obj_detect.model_id))
    print("Labels:\n{}\n".format(obj_detect.labels))

    fps = edgeiq.FPS()

    try:
        with edgeiq.WebcamVideoStream(cam=0) as video_stream, \
                edgeiq.Streamer() as streamer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()

            while True:
                frame = video_stream.read()
                results = obj_detect.detect_objects(frame, confidence_level=.5)
                people = edgeiq.filter_predictions_by_label(
                        results.predictions, ['person'])
                tracked_people = tracker.update(people)

                people = []
                for (object_id, prediction) in tracked_people.items():
                    new_label = 'Person {}'.format(object_id)
                    prediction.label = new_label
                    people.append(prediction)

                frame = edgeiq.markup_image(
                        frame, people, colors=obj_detect.colors)

                if new_detection:
                    save_snapshot(frame)
                new_detection = False

                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))
                text.append("Objects:")

                for prediction in people:
                    text.append("{}: {:2.2f}%".format(
                        prediction.label, prediction.confidence * 100))

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
