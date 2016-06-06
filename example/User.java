package example;

public class User extends AbstractUser {

	public static class Builder extends AbstractUser.Builder<User> {

		@Override
		public User build() {
			return new User(this);
		}
	}

	private User(Builder builder) {
		surname = builder.surname;
		name = builder.name;
		luckynumbers = builder.luckynumbers;
		age = builder.age;
		hasage = builder.hasage;
		phone = builder.phone;
		hasphone = builder.hasphone;
		hobbies = builder.hobbies;
	}
}
