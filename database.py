# import sqlalchemy
from sqlalchemy import create_engine, text

# print(sqlalchemy.__version__)

import os
import asyncio
from sqlalchemy import text
from dotenv import load_dotenv
from urllib.parse import urlparse
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()

tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
# my_secret = os.environ['DATABASE_URL']


# engine = create_engine(f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require", echo=True)
# async def async_main() -> None:
# 	async with engine.connect() as conn:
# 		# result = await conn.execute(text("select 'hello world'"))
# 		result = await conn.execute(text("select * from jobs"))

# 		result_dicts = []
# 		for row in result.all():
# 			result_dicts.append(row._asdict())
			
# 		# print("type(result):", type(result))
# 		# result_all = result.all()
# 		# print("type(result_all):", type(result_all))
# 		# print("type(result_all[0]):", type(result_all[0]))
# 		# print(result.fetchall())
# 		# print(result_all)
# 		# print(result_dicts)
# 	await engine.dispose()

# asyncio.run(async_main())

# with engine.connect() as conn:
# 	result = conn.execute(text("select * from jobs"))
# 	print(result.fetchall())


async def load_jobs_from_db():
	engine = create_async_engine(f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require", echo=True)
	async with engine.connect() as conn:
		result = await conn.execute(text("select * from jobs"))
		jobs = []
		for row in result.all():
			jobs.append(row._asdict())
		# print(jobs)
		return jobs
	await engine.dispose()


