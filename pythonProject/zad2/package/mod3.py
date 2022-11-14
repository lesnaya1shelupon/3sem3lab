if __name__ == '__main__':
    def table_nam(kykes):
        post = []
        for idx_new, spisok_new_new in enumerate(kykes, 1):
            post.append(
                '| {:>4} | {:<15} | {:<30} | {:<20} | {:<15} | '.format(
                    idx_new,
                    spisok_new_new.get('data', ''),
                    spisok_new_new.get('surname', ''),
                    spisok_new_new.get('name', ''),
                    spisok_new_new.get('post', 0) 
                    )
                )
        return post
