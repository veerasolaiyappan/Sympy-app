# Sympy-app
Sympy gamma api development using flask 

This application is proposed for providing Mathematical related HTML format files as Json objects through  API 


# How to Sympy app in our local host 

## Clone the Sympy app Project from Github
  
  Open your terminal and Type 
  `git clone https://github.com/newlinedeveloper/Sympy-app.git`

## Create Python Virtual Environment
  
  After clone Project then Create Virtual environment
  
  ```
      python3 -m pip install --user virtualenv
      
  ```
  Activate Virtual Environment
  ```
    source ./sympy/bin/activate
  ```
  
  Deactivate the Virtual Environmet
  ```
  deactivate
  ```

## Install Requirement packages

Install requirements packages which are available in requirements.txt file

```
  pip install -r requirements.txt
```


## Run the Sympy app

```
  flask run
```

## Api

### Integration
``` 
  http://localhost:5000/sympy/?exp=integrate
```
### Simplification
```
  http://127.0.0.1:5000/sympy/?exp=simplification
```

### Factorial
```
  http://127.0.0.1:5000/sympy/?exp=factorial
```


