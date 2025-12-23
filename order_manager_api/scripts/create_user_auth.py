from ..models.user import User 
from ..config.database import db_manager
import secrets

def main():
    name = input("Enter user name: ").strip()
    email = input("Enter user email: ").strip()
    
    user = User(
        name=name,
        email=email,
        token=secrets.token_hex(64)
    )
    
    session = db_manager.get_session()
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    print(f"User created: {user.email}")
    print(f"Token: {user.token}")

if __name__ == "__main__":
    main()