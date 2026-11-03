def lambda_handler(event, context):
    name = event.get("name", "World")
    return {"greeting": f"Hello, {name}!"}
