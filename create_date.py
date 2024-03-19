# from main import Database
# def table():
#     menyu_table = """
#         CREATE TABLE menu(
#             menyu_id serial PRIMARY KEY,
#             name varchar(20),
#             create_table timestamp default now())
#     """
#
#     category_table = """
#         CREATE TABLE category(
#             category_id serial PRIMARY KEY,
#             name varchar(20),
#             create_table timestamp default now())
#     """
#
#     data = {
#         "menyu": menyu_table,
#         "category":category_table
#     }
#     for i in data:
#         print(f"{i} - {Database.connect(data[i], 'create')}")
#
#
#
# if __name__ == "__main__":
#     table()