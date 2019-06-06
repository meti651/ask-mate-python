create table question_tag
(
    question_id integer not null
        constraint fk_question_id
            references question
            on delete cascade,
    tag_id      integer not null
        constraint fk_tag_id
            references tag
            on delete cascade,
    constraint pk_question_tag_id
        primary key (question_id, tag_id)
);

alter table question_tag
    owner to shadyhu1;

INSERT INTO public.question_tag (question_id, tag_id) VALUES (0, 1);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (1, 3);