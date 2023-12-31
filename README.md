﻿# Django-Redis-InMemoryStorageHandler


1. Clone the repository:
   ```bash
   git clone https://github.com/hale2024/Django-Redis-InMemoryStorageHandler.git
   ```

2. Change to the cloned repository directory:
   ```bash
   cd Django-Redis-InMemoryStorageHandler
   ```

3. Install the required package using pip:
   ```bash
   pip install django4-background-tasks
   ```

4. Start the Docker containers in detached mode:
   ```bash
   docker-compose up -d
   ```

5. Run the Django server:
   ```bash
   python manage.py runserver
   ```

   Note: If you visit the page, you may not see anything displayed.

6. Allows the use of the RefreshHandler function for Background Task handling:
   ```bash
   python manage.py process_tasks
   ```

7. Run the tests:
   ```bash
   python manage.py test
   ```

Files to check related to the in-memory cache:

- `src/refreshHandler.py`
- `src/requestHandler.py`
- `src/tests.py`
- `src/app.py` (calls the `refreshHandler`)
- `src/urls.py`
- `Redis/settings.py` (refer to [this link](https://www.dragonflydb.io/faq/how-to-use-redis-with-django) for more information)

