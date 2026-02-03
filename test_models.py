"""
測試所有模型是否可用
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_KEY"),
)

# 所有待測試的模型
MODELS = [
    # lawful
    "openai/gpt-4o-mini",
    "openai/gpt-4o",
    "anthropic/claude-3.5-sonnet",
    "anthropic/claude-3-haiku",
    
    # chaotic
    "meta-llama/llama-3.1-8b-instruct",
    "meta-llama/llama-3.1-70b-instruct",
    "meta-llama/llama-3.1-405b-instruct",
    "mistralai/mistral-7b-instruct",
    "mistralai/mistral-large",
    "mistralai/mixtral-8x7b-instruct",
    "google/gemma-2-9b-it",
    "google/gemma-2-27b-it",
    "deepseek/deepseek-chat",
    "qwen/qwen-2.5-72b-instruct",
    "mistralai/mistral-nemo",
    "x-ai/grok-3-mini",
    
    # uncensored
    "nousresearch/hermes-3-llama-3.1-405b:free",
    
    # experimental
    "meta-llama/llama-3-8b-instruct",
    "meta-llama/llama-3.2-3b-instruct",
    "microsoft/wizardlm-2-8x22b",
]

print("🔍 開始測試模型...\n")
print("=" * 70)

working_models = []
failed_models = []

for i, model in enumerate(MODELS, 1):
    print(f"\n[{i}/{len(MODELS)}] 測試: {model}")
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": "Hi"}
            ],
            max_tokens=5,
            temperature=0.3,
        )
        
        content = response.choices[0].message.content
        print(f"  ✅ 成功: {content[:30]}...")
        working_models.append(model)
        
    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg:
            print(f"  ❌ 失敗 (404): 模型不存在或不可用")
        elif "429" in error_msg:
            print(f"  ⏳ 失敗 (429): Rate limit (可能臨時性)")
        else:
            print(f"  ❌ 失敗: {error_msg[:80]}")
        
        failed_models.append((model, error_msg))

print("\n" + "=" * 70)
print("\n📊 測試結果:")
print(f"  ✅ 可用模型: {len(working_models)} 個")
print(f"  ❌ 失敗模型: {len(failed_models)} 個")

if working_models:
    print("\n✅ 可用模型清單:")
    for model in working_models:
        print(f"  - {model}")

if failed_models:
    print("\n❌ 失敗模型清單:")
    for model, error in failed_models:
        if "404" in error:
            print(f"  - {model} (404 - 不存在)")
        elif "429" in error:
            print(f"  - {model} (429 - Rate limit)")
        else:
            print(f"  - {model} (其他錯誤)")

print("\n" + "=" * 70)
print(f"\n最終可用模型數量: {len(working_models)}/20")

if len(working_models) < 20:
    print(f"\n⚠️ 需要替換 {20 - len(working_models)} 個模型")
