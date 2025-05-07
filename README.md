# 学習記録用

## 参考サイト

- [\[Python\] Djangoチュートリアル - 汎用業務Webアプリを最速で作る](https://qiita.com/okoppe8/items/54eb105c9c94c0960f14#%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%89-1)
- [Djangoのフォーム（forms.py）を使ってデータを作成し、記録する（基礎の基礎３）](https://qiita.com/ykoji/items/4d4a1230724acc1b7c95)

## 公式リンク
- [Overview](https://docs.djangoproject.com/ja/5.1/intro/overview/)
- [Generic View](https://docs.djangoproject.com/ja/2.1/ref/class-based-views/)
- [Multiple Object Mixin](https://docs.djangoproject.com/ja/5.1/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset)

## Django plugins
- [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
- [django-filter](https://django-filter.readthedocs.io/en/stable/)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [django-tables2](http://django-tables2.readthedocs.io/en/latest/index.html)
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/)
- [django-rest-framework](https://www.django-rest-framework.org/)
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/)
- [simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [django-taggit](https://django-taggit.readthedocs.io/en/latest/)
- [django-otp](https://django-otp-official.readthedocs.io/en/stable/)

## setup

### Django app

1. `python -m venv venv`
1. `.\venv\Scripts\activate`
1. `pip install --upgrade pip`
1. `pip install Django`
1. `django-admin startproject learning_manager .`
1. start app

    ```sh
    python manage.py startapp app
    python manage.py startapp apiv1
    ```

### front app

nvmやpnpmのインストール

```sh
# nvmをダウンロードしてインストールする
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
# シェルを再起動する代わりに実行する
\. "$HOME/.nvm/nvm.sh"
# Node.jsをダウンロードしてインストールする
nvm install 24
# Node.jsのバージョンを確認する
node -v # "v24.0.0"が表示される。
nvm current # "v24.0.0"が表示される。
# pnpmをダウンロードしてインストールする
corepack enable pnpm
# pnpmのバージョンを確認する
pnpm -v
# Vueアプリ作成
pnpx create-vite
# インストール
cd frontend
pnpm install
# 起動
pnpm run dev
```


## memo

### 起動  
`python manage.py runserver`

### DBのテーブル作成  
デフォルトで利用するアプリ(settings.py)もDBを使うので初回も実行する  
`python manage.py migrate`

### 新規モデルの作成  
マイグレーションを作成し、実行する  
`python manage.py makemigrations && python manage.py migrate`

### superuser作成  
`python manage.py createsuperuser`

### モデル変更時にmigrateでエラーが出たとき  
```
python manage.py showmigrations
python manage.py migrate app zero --fake
※zero: すべてのマイグレーション
  fake: `no such table` 等のエラーでこけるのを防ぐために、実行したことにするオプション
python manage.py migrate
```

### URLの解決チェック
```sh
python manage.py show_urls

python manage.py shell

from django.urls import reverse
reverse("【URLパターンの名前】", args=[1])
```
