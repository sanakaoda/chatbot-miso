import streamlit as st
import requests  # APIリクエスト用ライブラリ

# APIのURLを定義
api_url = ""


# アプリのタイトルと説明
st.title("💬 CS Chatbot ")
st.write(
    "このアプリでは、指定されたAPIを使用してプロンプトに対する応答を生成します。"
)

# プロンプト入力フィールド
prompt = st.text_input("プロンプトを入力してください:")

# プロンプトが入力された場合にAPIを呼び出す
if prompt:
    # APIリクエストのボディを作成
    request_body = {
        "user_utterance": prompt,
        "model": "gpt-4o"
    }

    # APIリクエストを送信
    try:
        response = requests.post(api_url, json=request_body, verify=False)
        if response.status_code == 200:
            # レスポンスの内容を取得
            result = response.json()  # JSONレスポンスを取得
            
            # レスポンス全体を可視化
            # st.write("### レスポンス全体:")
            # st.json(result)  # JSON形式でレスポンス全体を表示
            
            # ネストされた構造から final_response を取得
            dialogue_history = result.get("dialogue_history", {})  # 上位のキー "dialogue_history" を取得
            generate_final_response = dialogue_history.get("generate_final_response", {})  # "generate_final_response" を取得
            final_response = generate_final_response.get("final_response", "応答が見つかりませんでした。")  # "final_response" を取得
            
            st.write("### 応答:")
            st.write(final_response)  # final_response のみを表示
        else:
            st.error(f"エラー: ステータスコード {response.status_code}")
    except Exception as e:
        st.error(f"APIリクエスト中にエラーが発生しました: {e}")
