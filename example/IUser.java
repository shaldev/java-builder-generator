package example;

import java.util.List;

public interface IUser {

	public boolean hasSurname();
	public String getSurname();
	public boolean hasName();
	public String getName();
	public boolean hasLuckynumbers();
	public List<Integer> getLuckynumbers();
	public boolean hasAge();
	public int getAge();
	public boolean hasPhone();
	public int getPhone();
	public boolean hasHobbies();
	public List<String> getHobbies();
}
