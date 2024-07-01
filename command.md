pip freeze > requirements.txt
chmod +x ./entrypoint.sh
docker-compose up -d --build
docker exec -it django /bin/sh
python manage.py shell

# Remove all docker
docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -aq)

task grouping modelleri aynı anda çalıştırmak için kullanışlı olabilir
task chaining ise model analizinden çıkarn sonuçları after processe e aktarırken kullanılabilir

from celery import group
from newapp.tasks import tp1, tp2, tp3, tp4, tp5, task1
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()

task_chain = chain(tp1.s(5), tp2.s(), tp3.s())
task_chain.apply_async()

task_rate_limit: belirli bir Celery görevinin belirli bir süre içinde ne kadar sıklıkla çalıştırılabileceğini tanımlar. Bu limit, görevin çalıştırılma sıklığını kontrol eder ve gerektiğinde görevin yürütülmesini geciktirir.