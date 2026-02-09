SELECT * from titanic;
SELECT Name from titanic WHERE Age > 30;
SELECT Name from titanic WHERE Sex='female' and pclass=1;
SELECT Name,Age from titanic WHERE Survived=1 ORDER BY Age;
SELECT Name from titanic WHERE SibSp=0 and Parch=0;
SELECT Name,Pclass from titanic WHERE Fare>100;
SELECT Name,Pclass,Age from titanic WHERE Pclass!=1 and Age>18;
SELECT * from titanic WHERE Survived=0 and SibSp=0 and Parch=0;
SELECT Name,Pclass,Fare from titanic WHERE Fare<10 and Pclass!=3;