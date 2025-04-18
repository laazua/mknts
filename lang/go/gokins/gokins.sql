-- 创建rbac表
CREATE TABLE "user" (
  id bigint primary key generated always as identity,
  name text not null,
  email text not null unique,
  password text not null,
  avatar text,
  token text unique,
  is_delete BOOLEAN DEFAULT FALSE
);

CREATE TABLE "role" (
  id bigint primary key generated always as identity,
  name text not null unique,
  description text
);

CREATE TABLE "menu" (
  id bigint primary key generated always as identity,
  name text not null unique,
  redirect text not null,
  path text not null,
  component text not null,
  parent_id bigint not null,
  meta JSONB not null,
  description text
);


CREATE TABLE "user_role" (
  user_id bigint references "user" (id) on delete cascade,
  role_id bigint references "role" (id) on delete cascade,
  primary key (user_id, role_id)
);

CREATE TABLE "role_menu" (
  role_id bigint references "role" (id) on delete cascade,
  permission_id bigint references "menu" (id) on delete cascade,
  primary key (role_id, permission_id)
);

-- 查询用户权限
select
  u.username,
  r.name as role_name,
  m.name as menu_name
from
  "user" u
  join user_role ur on u.id = ur.user_id
  join "role" r on ur.role_id = r.id
  join role_menu rm on r.id = rm.role_id
  join menu m on rm.permission_id = m.id
where
  username = 'zhangsan';