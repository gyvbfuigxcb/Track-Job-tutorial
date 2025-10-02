import streamlit as st
# 投稿内容を保存するリストを作成
if 'posts' not in st.session_state:
    st.session_state.posts = []


# アプリケーションのタイトル
st.title('シンプルなX(旧Twitter)風アプリ')

# テキスト入力欄
post_content = st.text_input('あなたの投稿を入力してください:')

# 投稿ボタン
if st.button('投稿する'):
       if post_content:  # 投稿内容が空でない場合
        st.success('投稿が完了しました！') #投稿完了の通知
        st.session_state.posts.append(post_content) # リストに保存
else:  # 投稿内容が空の場合
        st.warning('投稿内容を入力してください。')  # アラートを表示

# 投稿内容を表示
for post in st.session_state.posts:
    st.text_area('投稿内容',post)
