#### 用户表(sys_user)  

| 字段名称 | 字段 | 类型 | 备注 |
| :----: | :----: | :----: | :----: |  
| 主键 | id | bigint | pk, not null |  
| 所属用户组 | user_group_id | bigint | fk, not null |  
| 用户名 | username | varchar(64) | not null |
| 用户密码 | password | varchar(64) | not null |  
| 盐值 | salt | varchar(64) | not null |  
| 姓名 | name | varchar(64) | not null |  
| 电话 | phone | varchar(20) |  |  
| 邮箱 | email | varchar(64) |  |  
| 创建时间 | create_time | datetime |  |  
| 更新时间 | update_time | datetime |  |  
| 创建人 | create_id | bigint |  |  
| 更新人 | update_id | bigint |  |
| 登录时间 | login_time | datetime |  |  
| 上次登录时间 | last_login_time | datetime |  |  
| 登录次数 | login_num | bigint | not null |  


#### 角色表(sys_role)  

| 字段名称 | 字段 | 类型 | 备注 |  
| :----: | :----: | :----: | :----: |  
| 主键 | id | bigint | pk, not null |  
| 角色名称 | name | varchar(64) | not null |  
| 创建时间 | create_time | datetime |  |  
| 更新时间 | update_time | datetime |  |  
| 创建人 | create_id | bigint |  |  
| 更新人 | update_id | bigint |  |
| 角色描述 | description | varchar(200) |  |  


#### 权限表(sys_permission)  

| 字段名称 | 字段 | 类型 | 备注 |  
| :----: | :----: | :----: | :----: |  
| 主键 | id | int(11) | pk, not null, auto_increment |   
| 模块 | module | varchar(30) | not null |  
| 模块名称 | module_name | varchar(50) | not null |  
| 操作 | action | varchar(20) | not null |   
| 权限描述 | description | varchar(128) |   |  
| 创建时间 | create_time | datetime |   |
| 更新时间 | update_time | datetime |   |  
| 创建人 | create_id | bigint |   |  
| 更新人 | update_id | bigint |   |


#### 用户组表(sys_user_group)  

| 字段名称 | 字段 | 类型 | 备注 |  
| :----: | :----: | :----: | :----: |  
| 主键 | id | bigint | pk, not null |  
| 用户组名称 | name | varchar(64) | not null |  
| 父用户组 | parent_id | bigint | not null |  
| 创建时间 | create_time | datetime |   |  
| 更新时间 | update_time | datetime |   |  
| 创建人 | create_id | bigint |   |  
| 更新人 | update_id | bigint |   |
| 用户组描述 | description | varchar(200) |   |  


#### 角色权限关联表(sys_role_permission)  

| 字段名称 | 字段 | 类型 | 备注 |  
| :----: | :----: | :----: | :----: |  
| 主键 | id | bigint | pk, not null |  
| 角色 | role_id | bigint | fk, not null |  
| 权限 | permission_id | bigint | fk, not null |  


#### 用户组角色关联表(sys_user_group_role)  

| 字段名称 | 字段 | 类型 | 备注 |  
| :----: | :----: | :----: | :----: |  
| 主键 | id | bigint | pk, not null |  
| 用户组 | user_group_id | bigint | fk, not null |  
| 角色 | role_id | bigint | pk, not null |   


#### 用户角色关联表(sys_user_role)  

| 字段名称 | 字段 | 类型 | 备注 |  
| :----: | :----: | :----: | :----: |  
| 主键 | id | bigint | pk, not null |  
| 用户 | user_id | bigint | fk, not null |  
| 角色 | role_id | bigint | fk, not null |


#### 用户用户组关联表(sys_user_group)  

| 字段名称 | 字段 | 类型 | 备注 |  
| :----: | :----: | :----: | :----: |  
| 主键 | id | bigint | pk, not null |  
| 用户 | user_id | bigint | fk, not null |  
| 用户组 | user_group_id | bigint | fk, not null |