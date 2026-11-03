def lambda_handler(event, context):
    a = event.get("a", 0)
    b = event.get("b", 0)
    return {"sum": a + b}
