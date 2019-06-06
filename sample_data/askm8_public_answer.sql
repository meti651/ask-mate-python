create table answer
(
    id              serial not null
        constraint pk_answer_id
            primary key,
    submission_time timestamp,
    vote_number     integer,
    question_id     integer
        constraint fk_question_id
            references question
            on delete cascade,
    message         text,
    image           text,
    username        text,
    user_id         integer
        constraint user_id
            references users
            on delete cascade
);

alter table answer
    owner to shadyhu1;

INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, username, user_id) VALUES (1, '2017-04-28 16:49:00.000000', 4, 1, 'You need to use brackets: my_list = []', null, 'admin', 1);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, username, user_id) VALUES (2, '2017-04-25 14:42:00.000000', 35, 1, 'Look it up in the Python docs', 'images/image2.jpg', 'admin', 2);