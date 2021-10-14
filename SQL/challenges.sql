-- https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
-- 서브쿼리로 challenge의 개수 산출
-- challenge 개수 토대로 필터
-- 최댓값 아니면서 challenge 개수가 중복되는 행 제거

select A.hacker_id, A.name, A.num
from
(select H.hacker_id, H.name, count(C.challenge_id) as num
from hackers H inner join challenges C
on H.hacker_id = C.hacker_id
group by h.hacker_id, h.name) A
where A.num in
(select max(A.num) from (select H.hacker_id, H.name, count(C.challenge_id) as num
from hackers H inner join challenges C
on H.hacker_id = C.hacker_id
group by h.hacker_id, h.name) A)
or A.num in
(select A.num from (select H.hacker_id, H.name, count(C.challenge_id) as num
from hackers H inner join challenges C
on H.hacker_id = C.hacker_id
group by h.hacker_id, h.name) A group by A.num
having count(*) = 1)
order by A.num desc, A.hacker_id;