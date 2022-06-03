# Fastapi_with_flask

## Установка

- Клонируем репозиторий

  ```bash
  git clone https://github.com/ilyailyushko/fastapi_with_flask.git
  ```

- Устанавливаем fastapi и uvicorn

  ```bash
  pip install fastapi
  pip install "uvicorn[standard]"
  ```

- Устанавливаем flask

  ```bash
  pip install Flask
  ```

-  Устанавливаем библиотеку для работы с б24

  ```
  pip install fast-bitrix24
  ```

  

## Запуск

```
uvicorn main:app --host 194.67.119.72 --port 80 --reload
```

*Если не нужна перезагрузка при изменении файлов, снять флаг `--reload`*



