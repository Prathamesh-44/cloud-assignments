from datetime import datetime, timezone


def lambda_handler(event, context):
    return {"utc_now": datetime.now(timezone.utc).isoformat()}
