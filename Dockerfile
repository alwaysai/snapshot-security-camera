ARG ALWAYSAI_HW="default"
FROM alwaysai/edgeiq:${ALWAYSAI_HW}-2.2.1
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


