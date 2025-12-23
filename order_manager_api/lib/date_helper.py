

class DateHelper:
    @staticmethod
    def utcnow():
        """Returns the current time in UTC."""
        from datetime import datetime, timezone
        return datetime.now(timezone.utc)