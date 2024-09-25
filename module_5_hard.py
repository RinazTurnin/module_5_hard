import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname: str = nickname
        self.password: int = hash(password)
        self.age: int = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title: str = title
        self.duration: int = duration
        self.time_now: int = time_now
        self.adult_mode: bool = adult_mode


class UrTube:
    def __init__(self, users=None, videos=None, current_user: User = None):
        if videos is None:
            videos = []
        if users is None:
            users = []
        self.users: list[User] = users
        self.videos: list[Video] = videos
        self.current_user: User = current_user

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and hash(password) == user.password:
                self.current_user = user
                break

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *new_videos: Video):
        for new_video in new_videos:
            for video in self.videos:
                if new_video.title == video.title:
                    break
            else:
                self.videos.append(new_video)

    def get_videos(self, searcher: str):
        searcher = searcher.lower()
        titles = []
        for video in self.videos:
            if video.title.lower().find(searcher):
                titles.append(video.title)
        return titles

    def watch_video(self, title: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if title == video.title:
                video_to_watch = video
                break
        else:
            return
        if video_to_watch.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for second in range(video_to_watch.time_now, video_to_watch.duration + 1):
            if not second:
                continue
            print(second, end=' ')
            video_to_watch.time_now = second
            time.sleep(1)
        print('Конец видео.')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
