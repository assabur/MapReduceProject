# Description

MapReduceProject is a Python project understand a map reduce concept.

## Installation

Use git to clone project.
```bash
git clone https://github.com/assabur/MapReduceProject.git
```

## Usage
Make sure mapper.py combine.py reducer.py have the right to execute
if not the case 
```Make chmod +x mapper.py combine.py reducer.py```

```python
cat users.txt calls.txt |./mapper.py|./combine.py |./reducer.py > resultat.txt
```

## Output
```python
Make chmod +x mapper.py combine.py reducer.py```

```python
Andrew has an average time of 43.27 with 1196 calls
Liam has an average time of 45.65 with 2012 calls
Luke has an average time of 44.52 with 1153 calls
Michael has an average time of 44.75 with 1459 calls
Natalie has an average time of 44.08 with 460 calls
William has an average time of 45.39 with 823 calls

``

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
