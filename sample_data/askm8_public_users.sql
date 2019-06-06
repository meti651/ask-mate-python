create table users
(
    id                serial            not null
        constraint pk_users_id
            primary key,
    user_name         text
        constraint users_user_name_key
            unique,
    password          text              not null,
    email             text
        constraint users_email_key
            unique,
    registration_time timestamp,
    reputation        integer default 0 not null
);

alter table users
    owner to shadyhu1;

INSERT INTO public.users (id, user_name, password, email, registration_time, reputation) VALUES (0, 'admin', 'admin', 'admin@admin.com', '2019-06-03 13:00:00.000000', 0);
INSERT INTO public.users (id, user_name, password, email, registration_time, reputation) VALUES (1, 'teszt', '$2b$12$YDyd0EGt/cIDwTCUdpuOFunqSIC5wn8hfDoBaZty2CW68i2mvP936', 'asfdasfafasf@sdfsdf.com', '2019-06-06 10:54:05.000000', 0);
INSERT INTO public.users (id, user_name, password, email, registration_time, reputation) VALUES (2, 'admin1', '$2b$12$T9KyvWti3lB/ZhG62ORHrujTTWIOc5TYeJ1XbLbVquRSNWuHELKTO', 'yxcyxcyxc@sdfsdf.com', '2019-06-06 11:23:10.000000', 21);