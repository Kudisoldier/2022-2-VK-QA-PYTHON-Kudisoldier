# VK SDET homeworks


## Final project - testing web app
Steps to run final project:  
```
brew services start jenkins  
```
Run docker  
Go to http://localhost:6969  
Click "Build Now"

Contents:
- 8 smoke tests
- Api tests
- UI tests
- DB tests

Features:
- CI: jenkins, docker
- Automatic allure reports
- Supports multithreading
- Written with PageObject pattern
- Used selenoid to run browsers
- Mock server for VKID with FastAPI

How I did the project:
https://cultured-banana-8e5.notion.site/900754a17b764dc99b63b7cfbdd3974a

Test-plan:
https://cultured-banana-8e5.notion.site/f8f400eaa1c946f3a7d0eebd78dd8b4c

Test-cases:
https://cultured-banana-8e5.notion.site/0b9aaa6c347b490fbb5691b1b785fb1a

Bug-tracker:
https://cultured-banana-8e5.notion.site/dcb0bb9418dc46e0960ddbeaf2eebd89?v=436cb03e77d741a98f2e8f443321b642

Checklist:
https://cultured-banana-8e5.notion.site/cde49e4919394d12b7442562a1adf641?v=8010da95e35746799c81323afa8e5ccc


## Homework 1 - testing web UI with selenium
Steps to run homework1:
```
pytest homework1 -m UI --headless
```

Contents:
- login test
- logout test
- 2 login negative test
- change contacts test
- 2 parametrized menu page navigation

## Homework 2 - testing web UI with selenium and PageObject pattern
Steps to run homework2:
```
pytest homework2 -m UI --headless -n 3 --alluredir allure
```
Steps to view allure report:
```
allure serve allure
```
Steps to run selenoid:
```
add --selenoid option to pytest
./cm_darwin_amd64 selenoid-ui start

pytest --selenoid -n 3

OR for my mac m1

docker run -d                                   \
--name selenoid                                 \
-p 4444:4444                                    \
-v /var/run/docker.sock:/var/run/docker.sock    \
-v `pwd`/config/:/etc/selenoid/:ro              \
--privileged                                    \
aerokube/selenoid:latest-release                \
-service-startup-timeout 1m

docker run -d         \
    --name selenoid-ui  \
    --link selenoid     \
    -p 8080:8080        \
    aerokube/selenoid-ui --selenoid-uri=http://selenoid:4444
```

Contents:
- advertising campaign test
- creation of segment with audience in app test
- creation of segment with vk edu group test

Features:
- runnable in selenoid
- support multiple CPU runs
- automatic allure reports
- written with PageObject pattern
- login with api call

## Homework 3 - testing website with API
Steps to run homework3:
```
cd homework 3
pytest -m API
```

Contents:
- advertising campaign test
- creation of segment with audience in app test
- creation of segment with vk edu group test

Features:
- support multiple CPU runs
- written with PageObject pattern

## Homework 4 - testing android UI with appium
Steps to run homework4:
```
run phone emulator with Adnroid Studio
run appium server with settings
pytest homework4 -m AndroidUI
```

Contents:
- command window test
- calculator test
- news source test
- settings test

## Homework 5 - writing scripts
Steps to run homework5:  
All scripts should be run from repository root folder  
Set up your path variable as follows:
```
export PATH_TO_LOG_FILE=setup_your_path.log
```
Then run one of these scripts like that

```
./path/script.bash <path_to_log_file>
OR
python3 ./path/script.py <path_to_log_file> --json
--json is optional
```

Copy-paste commands:
```
./task1/count_requests.bash $PATH_TO_LOG_FILE
python3 ./task1/count_requests.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task1/count_requests.py $PATH_TO_LOG_FILE --json

./task2/count_requests_type.bash $PATH_TO_LOG_FILE
python3 ./task2/count_requests_type.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task2/count_requests_type.py $PATH_TO_LOG_FILE --json

./task3/top_frequent_requests.bash $PATH_TO_LOG_FILE
python3 ./task3/top_frequent_requests.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task3/top_frequent_requests.py $PATH_TO_LOG_FILE --json

./task4/top_biggest_requests.bash $PATH_TO_LOG_FILE
python3 ./task4/top_biggest_requests.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task4/top_biggest_requests.py $PATH_TO_LOG_FILE --json

./task5/top_user_requests_failed.bash $PATH_TO_LOG_FILE
python3 ./task5/top_user_requests_failed.py $PATH_TO_LOG_FILE
OR with optional flag --json
python3 ./task5/top_user_requests_failed.py $PATH_TO_LOG_FILE --json
```


Contents:
- log requests count (task1)
  - \<number>
- requests type count (task2)
  - \<method> \<count>
- top 10 frequent requests (task3)
  - \<location>
  - \<number count>
- top 5 biggest requests with 4XX error (task4)
  - \<url>
  - \<status code>
  - \<size in bytes>
  - \<ip address>
- top 5 users with requests ended 5XX error (task5)
  - \<ip address>
  - \<requests count>

## Homework 6 - testing database with ORM
Steps to run homework6:
```
docker run --name TEST_SQL -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass -d mysql:8.0
pytest homework6 -n 2
```

Contents:
- All data from HW 5 tested

Features:
- support multiple CPU runs
- test written with pytest
- used MySql database

## Homework 7 - Http mock
Steps to run homework7:
```
sudo pytest homework7 -n 2
```

Contents:
- mock/app/stub tests
- mock logging to mock.log

Features:
- support multiple CPU runs
- written with PageObject pattern
- server written with uvicorn&fastapi
