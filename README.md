# course-tracker
Track you personal courses or learning, using a unit of your choice.

![image](./App0.png)
![image](./App1.png)

To execute, run the 'sg.py' file. (Make sure you have PySimpleGUI installed as well)

```console
pip install PySimpleGUI
python3 ./sg.py
```
### Edit courses
By leaving any field empty, it will remain as the old one.
### Add courses
You just need to provide a Name, Current Progress, Goal, Unit and a Tracking.
### Delete courses
Delete the course(s) you want by selecting it.
### Change 'Tracking'
You can alter between seeing you progress as a 'Percent' or as 'Stars'.
- Example: %90 or ★★★★☆
- Another example: %45 or ★★☆☆☆

| Percentage | Stars Representation |
|---|---|
| %0 | ☆☆☆☆☆ |
| %1-20 | ★☆☆☆☆ |
| %21-40 | ★★☆☆☆ |
| %41-60 | ★★★☆☆ |
| %61-99 | ★★★★☆ |
| %100 | ★★★★★ |
