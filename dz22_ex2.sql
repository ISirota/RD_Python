select purchase.id, purchase.date, users.first_name, users.last_name from purchase join users on purchase.user_id = users.id