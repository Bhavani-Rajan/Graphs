def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Use add_user num_users times

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # Generate all friendship combinations
        possible_friendships =  []

        # Avoid dupes by making sure first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle all possible friendships
        random.shuffle(possible_friendships)

        # Create for first X pairs x is total //2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # * Hint 1: To create N random friendships, you could create a
        # list with all possible friendship combinations, shuffle the
        # list, then grab the first N elements from the list. You will
        # need to `import random` to get shuffle.
        # * Hint 2: `add_friendship(1, 2)` is the same as
        # `add_friendship(2, 1)`. You should avoid calling one after
        # the other since it will do nothing but print a warning. You
        # can avoid this by only creating friendships where user1 < user2.