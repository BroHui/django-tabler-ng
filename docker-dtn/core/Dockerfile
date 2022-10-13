FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

RUN sed -i s@/deb.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list  && \
	sed -i "s@http://security.debian.org@http://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list && \
	apt-get clean
RUN apt-get update && \
    apt-get install -y \
	gcc make mariadb-client libmariadb-dev iputils-ping procps git

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/ \
	&& pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn 
RUN pip install -U pip \
	&& pip install "Django==3.2" mysqlclient uwsgi \
	&& rm -rf /root/.cache/pip/*

WORKDIR /app
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
	echo "Asia/Shanghai" >  /etc/timezone
ENV TZ="Asia/Shanghai"

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]
CMD ["uwsgi", "--chdir", "/app", \
    "--socket", ":3031", \
    "--module", "zbsxmathkit.wsgi", \
    "--listen", "4096", \
    "--master", \
    "--processes", "8", \
    "--thunder-lock", \
    "--harakiri", "30", \
    "--enable-threads", \
    "--http", ":8000", \
    "--vacuum", \
    "--stats", ":9191", \
    "--stats-http", \
    "--memory-report", \
	"--static-map", "/static=/usr/src/static", \
	"--static-map", "/media=/usr/src/media" \
	]
