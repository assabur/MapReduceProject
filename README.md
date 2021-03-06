# Description

MapReduceProject is a Python project to understand well a map reduce concept.
we have 02 mainly files users.txt and calls.txt.
The purpose is to return the average call duration for each user living in Paris.
The schematics of the two attached files are:

```python
users(nom, prenom, tel, dept, ville)
calls(de, vers, durée)

SELECT name, avg(duration)
FROM calls C, users U
WHERE C.de= U.tel AND city='Paris'.
GROUP BY name);
```
# Demarche
```
In the Mapper.py file we filter the received data so that we get the names of the people living
in Paris, their phone number and the duration of the call.this information is then transmitted 
to the combine.py file.

In the Combine.py file we get in two dictionaries the list of the users living in Paris and their
phone numbers and in the other one the list of the calls made and their call duration. 
A third dictionary which will contain a phone number associated with a table containing all the
call durations.Then we can easily calculate the total sum of the call durations made by a user
living in Paris.This information is transmitted to the Reducer.py file.

To finish in the Reducer.py file, you will have to average the durations per user and to display it.
```

## Installation

Use git to clone project.
```bash
git clone https://github.com/assabur/MapReduceProject.git
```
## Usage
Make sure mapper.py combine.py reducer.py have the right to execute
if not the case open a terminal and type
```python
Make chmod +x mapper.py combine.py reducer.py
cat users.txt calls.txt |./mapper.py|./combine.py |./reducer.py > resultat.txt
```

## Output
```python
Andrew has an average time of 43.27 with 1196 calls
Liam has an average time of 45.65 with 2012 calls
Luke has an average time of 44.52 with 1153 calls
Michael has an average time of 44.75 with 1459 calls
Natalie has an average time of 44.08 with 460 calls
William has an average time of 45.39 with 823 calls

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
