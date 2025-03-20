DROP TABLE IF EXISTS employees; 
-- 기존 잘못 만든 empioyees 데이터 삭제

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10,2)
);

INSERT employees (name, position, salary) VALUES 
('혜린', 'PM', 90000.00),
('은우', 'Frontend', 80000.00),
('가을', 'Backend', 92000.00),
('지수', 'Frontend', 78000.00),
('민혁', 'Frontend', 96000.00),
('하온', 'Backend', 130000.00);
-- employees 테이블에 직원데이터 추가

SELECT name, salary FROM employees;
-- 모든 직원의 이름과 연봉조회

SELECT name, salary 
FROM employees 
WHERE position = 'Frontend' AND salary <= 90000;
-- 프론트엔드 직책을 가진 직원 중 연봉이 90,000이하인 직원 조회

UPDATE employees 
SET salary = salary * 1.10 
WHERE position = 'PM';
SELECT * FROM employees WHERE position = 'PM';
-- PM 직책을 가진 직원의 연봉을 10% 인상 후 결과 확인


UPDATE employees 
SET salary = salary * 1.05 
WHERE position = 'Backend';
-- 백엔드 직책을 가진 직원의 연봉을 5%인상

DELETE FROM employees 
WHERE name = '민혁';
-- 민혁 사원의 데이터 삭제

SELECT position, AVG(salary) AS average_salary 
FROM employees 
GROUP BY position;
-- 포지션 별 평균 연봉 계산

DROP TABLE employees;
-- employees 테이블 삭제




