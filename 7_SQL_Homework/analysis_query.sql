--1 List the following details of each employee: employee number, last name, first name, gender, and salary.

SELECT a.emp_no, last_name,first_name, gender, salary
FROM employees as A
 LEFT JOIN salaries as B on A.emp_no=B.emp_no
GROUP BY  a.emp_no, last_name,first_name, gender, salary 
--2 List employees who were hired in 1986.

SELECT * FROM employees WHERE EXTRACT(YEAR FROM hire_date) = 1986

--3. List the manager of each department with the following information: department number, department name, 
		--the manager's employee number, last name, first name, and start and end employment dates.
		
SELECT f.dept_no, f.dept_name, f.emp_no, d.last_name, d.first_name, f.from_date, f.to_date
FROM employees d
	JOIN(SELECT b.dept_no, b.dept_name, a.emp_no, c.from_date, c.to_date
			FROM dept_manager A
				JOIN departments B ON A.dept_no=B.dept_no
				JOIN dept_emp C ON A.emp_no=C.emp_no
		 GROUP BY 1,2,3,4,5) f ON f.emp_no=d.emp_no
GROUP BY 1,2,3,4,5,6,7;

--4. List the department of each employee with the following information: employee number, last name, 
        --first name, and department name.
SELECT a.emp_no, a.last_name, a.first_name, c.dept_name
FROM employees a
	LEFT JOIN dept_emp b ON a.emp_no = b.emp_no
	INNER JOIN departments c ON c.dept_no =  b.dept_no
GROUP BY  a.emp_no, a.last_name, a.first_name, c.dept_name;

--5. List all employees whose first name is "Hercules" and last names begin with "B."

SELECT * FROM employees WHERE first_name IN('Hercules') AND last_name LIKE 'B%';

--6. List all employees in the Sales department, including their employee number, last name, 
      --first name, and department name.
SELECT emp.emp_no, emp.last_name, emp.first_name, dep.dept_name
FROM employees emp
	JOIN dept_emp ON dept_emp.emp_no = emp.emp_no 
	INNER JOIN departments dep ON dep.dept_no =  dept_emp.dept_no
WHERE dep.dept_name IN ('Sales')
GROUP BY emp.emp_no, emp.last_name, emp.first_name, dep.dept_name
--7. List all employees in the Sales and Development departments, including their employee number, 
     --last name, first name, and department name.
SELECT emp.emp_no, emp.last_name, emp.first_name, dep.dept_name
FROM employees emp
	JOIN dept_emp ON dept_emp.emp_no = emp.emp_no 
	INNER JOIN departments dep ON dep.dept_no =  dept_emp.dept_no
WHERE dep.dept_name IN ('Sales','Development')
GROUP BY emp.emp_no, emp.last_name, emp.first_name, dep.dept_name

--8. In descending order, list the frequency count of employee last names, 
     --i.e., how many employees share each last name.
SELECT last_name, COUNT(*) AS Count_LastName
FROM employees
GROUP BY last_name
ORDER BY Count_LastName DESC;
