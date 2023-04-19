/*pandas*
timezone = "America/Chicago"
parse_dates = { created_at = "%Y-%m-%d %h:%m:%s", updated_at = "%Y-%m-%d %h:%m:%s" }
index_col = ["created_at"]
[dtype]
user_name = "string"
user_id = "int64"
created_at = "datetime64[ns, UTC]"
 *pandas*/
select *
from history