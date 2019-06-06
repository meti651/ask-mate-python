create table comment
(
    id              serial not null
        constraint pk_comment_id
            primary key,
    question_id     integer
        constraint fk_question_id
            references question
            on delete cascade,
    answer_id       integer
        constraint fk_answer_id
            references answer
            on delete cascade,
    message         text,
    submission_time timestamp,
    edited_count    integer
);

alter table comment
    owner to shadyhu1;

INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (1, 0, null, 'Please clarify the question as it is too vague!', '2017-05-01 05:49:00.000000', null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (2, null, 1, 'I think you could use my_list = list() as well.', '2017-05-02 16:55:00.000000', null);