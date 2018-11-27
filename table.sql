create table pianke_user
(
	id int not null comment '用户ID'
		primary key,
	user_name varchar(100) null comment '用户名',
	city varchar(50) null comment '城市',
	client int null comment '客户端类型',
	description varchar(200) null comment '个人描述',
	register_from int null comment '注册源',
	gender int null comment '性别',
	addtime int not null comment '注册时间'
)
comment '片刻用户表' engine=InnoDB
;

