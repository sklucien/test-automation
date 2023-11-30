## Book service

### How to dev 
- install project requirements : `pip install --no-cache-dir -r requirements.txt`
- start fake book server : `docker-compose up`
- check books are well returned : `curl -X GET http://localhost:1080/books | json_pp`