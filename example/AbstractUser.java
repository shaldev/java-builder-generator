package example;

import org.apache.commons.lang3.builder.ReflectionToStringBuilder;
import java.util.ArrayList;
import java.util.List;

public abstract class AbstractUser implements IUser {

	protected String surname;
	protected String name;
	protected List<Integer> luckynumbers;
	protected int age;
	protected boolean hasage;
	protected int phone;
	protected boolean hasphone;
	protected List<String> hobbies;

	@Override
	public String getSurname() {
		return surname;
	}

	@Override
	public boolean hasSurname() {
		return surname != null;
	}

	@Override
	public String getName() {
		return name;
	}

	@Override
	public boolean hasName() {
		return name != null;
	}

	@Override
	public List<Integer> getLuckynumbers() {
		return luckynumbers;
	}

	@Override
	public boolean hasLuckynumbers() {
		return luckynumbers != null;
	}

	@Override
	public int getAge() {
		return age;
	}

	@Override
	public boolean hasAge() {
		return hasage;
	}

	@Override
	public int getPhone() {
		return phone;
	}

	@Override
	public boolean hasPhone() {
		return hasphone;
	}

	@Override
	public List<String> getHobbies() {
		return hobbies;
	}

	@Override
	public boolean hasHobbies() {
		return hobbies != null;
	}

	public abstract static class Builder<T> implements IBuilder<T> {
		protected String surname;
		protected String name;
		protected List<Integer> luckynumbers;
		protected int age;
		protected boolean hasage = false;
		protected int phone;
		protected boolean hasphone = false;
		protected List<String> hobbies;

		public Builder setSurname(String surname) {
			this.surname = surname;
			return this;
		}

		public Builder setName(String name) {
			this.name = name;
			return this;
		}

		public Builder addLuckynumbers(int luckynumbers) {
			if (this.luckynumbers == null) {
				this.luckynumbers = new ArrayList<>();
			}

			this.luckynumbers.add(luckynumbers);
			return this;
		}

		public Builder setLuckynumbers(List<Integer> luckynumbers) {
			this.luckynumbers = luckynumbers;
			return this;
		}

		public Builder setAge(int age) {
			this.hasage = true;
			this.age = age;
			return this;
		}

		public Builder setPhone(int phone) {
			this.hasphone = true;
			this.phone = phone;
			return this;
		}

		public Builder addHobbies(String hobbies) {
			if (this.hobbies == null) {
				this.hobbies = new ArrayList<>();
			}

			this.hobbies.add(hobbies);
			return this;
		}

		public Builder setHobbies(List<String> hobbies) {
			this.hobbies = hobbies;
			return this;
		}

		@Override
		public abstract T build();
	}

	@Override
	public String toString() {
		return ReflectionToStringBuilder.toString(this);
	}
}
