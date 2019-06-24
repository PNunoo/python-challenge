DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;


CREATE TABLE departments (
	dept_no varchar NOT NULL,
  	dept_name character varying(45) NOT NULL
); 
COPY departments
FROM '/Users/data/departments.csv' DELIMITER ',' CSV HEADER;

select * from departments limit 10;

CREATE TABLE dept_emp (
  	emp_no integer NOT NULL,
  	dept_no varchar NOT NULL,
  	from_date date,
  	to_date date
);
COPY dept_emp
FROM '/Users/data/dept_emp.csv' DELIMITER ',' CSV HEADER;

select * from dept_emp limit 10;

CREATE TABLE dept_manager (
  	dept_no varchar NOT NULL,
  	emp_no integer NOT NULL, 
	from_date date,
	to_date date
);

COPY dept_manager
FROM '/Users/data/dept_manager.csv' DELIMITER ',' CSV HEADER;

select * from dept_manager limit 10;


CREATE TABLE salaries (
	emp_no integer NOT NULL, 
    salary numeric NOT NULL,
    from_date date,
  	to_date date
);

COPY salaries
FROM '/Users/data/salaries.csv' DELIMITER ',' CSV HEADER;

select * from salaries limit 10;

CREATE TABLE titles (
	emp_no integer NOT NULL, 
    title character varying(50) NOT NULL,
    from_date date,
  	to_date date
);

COPY titles
FROM '/Users/data/titles.csv' DELIMITER ',' CSV HEADER;
select * from titles limit 10;


CREATE TABLE employees (
	emp_no integer NOT NULL, 
	birth_date date,
	first_name character varying(45) NOT NULL,
	last_name character varying(45) NOT NULL,
	gender character varying(6),
	hire_date date
);

COPY employees
FROM '/Users/data/employees.csv' DELIMITER ',' CSV HEADER;

select * from employees limit 10;
