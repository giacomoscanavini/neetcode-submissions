-- Write your query below
SELECT 
    student_id, 
    exam_id, 
    score
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY score DESC, exam_id ASC
        ) AS rank_val
    FROM Exam_results

)
WHERE rank_val = 1
