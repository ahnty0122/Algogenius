-- 4번 풀이 1. SET 명령문 쓰기
-- '='은 비교연산자로 SET 이외의 문장에서 값 대입할 수 없음
-- SET이외의 명령문에선 ':=' 사용해야함
SET @HOUR_IT = -1; 
SELECT @HOUR_IT := @HOUR_IT+1 AS 'HOUR', 
    (SELECT COUNT(*) 
        FROM ANIMAL_OUTS 
        WHERE HOUR(DATETIME) = @HOUR_IT) AS 'COUNT' 
    FROM ANIMAL_OUTS 
    WHERE @HOUR_IT < 23;

-- 4번 풀이 2. GROUPBY, RECURSIVE 반복문 사용
-- with recursive 테이블명 as(쿼리1 union all 쿼리2)select * from 테이블명
-- UNION ALL 두 쿼리 결과를 행으로 합쳐줌
-- 테이블 하나 만들고 기존 테이블과 LEFT OUTER JOIN 하는 방법
-- DATE_FORMAT: 시간을 원하는 형태로 반환하는 함수 %H, %h 등등
WITH RECURSIVE TIME AS
(SELECT 0 AS HOUR UNION ALL SELECT HOUR+1 FROM TIME WHERE HOUR<23)
SELECT HOUR, COUNT(ANIMAL_ID) COUNT FROM TIME
LEFT OUTER JOIN ANIMAL_OUTS ON (HOUR = DATE_FORMAT(DATETIME, '%H'))
GROUP BY HOUR;