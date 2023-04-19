/*pandas*
timezone = "America/Chicago"
index_col = ["created_at"]
[parse_dates]
created_at = "%Y-%m-%d %H:%M:%S"
updated_at = "%Y-%m-%d %H:%M:%S"
[dtype]
user_name = "string"
user_id = "int64"
created_at = "datetime64[ns, UTC]"
*pandas*/
select *
from history