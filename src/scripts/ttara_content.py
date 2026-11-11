"""Content added after the first release. Everything here is written for this app (no outside text).

NEW_SENTENCES and NEW_LISTENS go to the front of their lists so new material comes up first.
Bump CONTENT_VERSION whenever new material is put at the front: it sends everyone back to item 1 once.
"""

CONTENT_VERSION = 2

# Order = button order for the new categories (가족, 리액션), then additions to existing ones.
NEW_SENTENCES = [
    ("가족", "Good morning! Did you sleep well?", "좋은 아침! 잘 잤어?"),
    ("가족", "Breakfast is ready.", "아침 준비됐어."),
    ("가족", "Hurry up, or you'll be late.", "서둘러, 안 그러면 늦어."),
    ("가족", "Did you finish your homework?", "숙제 다 했어?"),
    ("가족", "How was school today?", "오늘 학교 어땠어?"),
    ("가족", "Can you help me with the dishes?", "설거지 좀 도와줄래?"),
    ("가족", "Dinner is ready!", "저녁 다 됐어!"),
    ("가족", "Let's watch a movie together.", "같이 영화 보자."),
    ("가족", "Don't forget to brush your teeth.", "양치하는 거 잊지 마."),
    ("가족", "I'm so proud of you.", "네가 정말 자랑스러워."),
    ("가족", "Thank you for helping me.", "도와줘서 고마워."),
    ("가족", "Good night. Sleep tight.", "잘 자. 푹 자."),
    ("리액션", "That's amazing!", "정말 멋지다!"),
    ("리액션", "No way!", "말도 안 돼!"),
    ("리액션", "Really? Tell me more.", "정말? 더 얘기해 줘."),
    ("리액션", "That makes sense.", "그거 말 되네."),
    ("리액션", "I know, right?", "그러니까 말이야!"),
    ("리액션", "Good for you!", "잘됐다!"),
    ("리액션", "Oh no, that's too bad.", "아이고, 안됐다."),
    ("리액션", "Me too.", "나도."),
    ("리액션", "What about you?", "너는 어때?"),
    ("리액션", "Sounds good to me.", "난 좋아."),
    ("여행", "A table for three, please.", "세 명 자리 부탁해요."),
    ("여행", "Can I see the menu, please?", "메뉴 좀 볼 수 있을까요?"),
    ("여행", "I'll have this one, please.", "이걸로 할게요."),
    ("여행", "I'm allergic to nuts.", "저는 견과류 알레르기가 있어요."),
    ("여행", "Can I try this on?", "이거 입어 봐도 돼요?"),
    ("여행", "Do you have this in a smaller size?", "이거 더 작은 사이즈 있나요?"),
    ("여행", "I don't feel well.", "몸이 안 좋아요."),
    ("여행", "Where is the nearest pharmacy?", "가장 가까운 약국이 어디예요?"),
    ("유튜브", "Hi everyone, welcome back to my channel.", "여러분 안녕하세요, 제 채널에 다시 오신 걸 환영해요."),
    ("유튜브", "Today I'm going to show you my favorite camping gear.", "오늘은 제가 제일 좋아하는 캠핑 장비를 보여 드릴게요."),
    ("유튜브", "Let me show you how it works.", "어떻게 작동하는지 보여 드릴게요."),
    ("유튜브", "This is my favorite part.", "이게 제가 제일 좋아하는 부분이에요."),
    ("유튜브", "It's really easy to set up.", "설치가 정말 쉬워요."),
    ("유튜브", "It's light and easy to carry.", "가볍고 들고 다니기 편해요."),
    ("유튜브", "I'll put the link in the description.", "링크는 설명란에 넣어 둘게요."),
    ("유튜브", "Let me know in the comments.", "댓글로 알려 주세요."),
    ("유튜브", "See you in the next video.", "다음 영상에서 만나요."),
    ("유튜브", "Have a great day!", "좋은 하루 보내세요!"),
]

# Lines: (who, en, ko); who "" is a single narrator, "A"/"B" are two voices.
NEW_LISTENS = [
    ("여행", "Boarding Announcement", "탑승은 몇 번 게이트에서 하나요?", "23번 게이트", [
        ("", "Good afternoon, passengers.", "승객 여러분, 안녕하세요."),
        ("", "Flight 702 to Vancouver is now boarding.", "밴쿠버행 702편이 지금 탑승을 시작합니다."),
        ("", "Please go to gate twenty-three.", "23번 게이트로 가 주십시오."),
        ("", "Families with small children may board first.", "어린 자녀를 동반한 가족은 먼저 탑승하실 수 있습니다."),
        ("", "Please have your passport and boarding pass ready.", "여권과 탑승권을 준비해 주십시오."),
    ]),
    ("여행", "Checking In at a Hotel", "아침 식사는 어디에서 하나요?", "2층", [
        ("A", "Hi, I'd like to check in. The name is Kim.", "안녕하세요, 체크인하려고요. 김이에요."),
        ("B", "Welcome. You're staying for two nights, right?", "어서 오세요. 2박 하시는 거죠?"),
        ("A", "Yes. Is breakfast included?", "네. 아침 식사 포함인가요?"),
        ("B", "It is. It's served on the second floor from seven.", "네. 7시부터 2층에서 드립니다."),
        ("A", "Great. And what's the Wi-Fi password?", "좋네요. 와이파이 비밀번호는요?"),
        ("B", "It's on the back of your room key.", "방 열쇠 뒷면에 있어요."),
    ]),
    ("여행", "Ordering at a Restaurant", "손님은 샐러드에서 무엇을 빼 달라고 했나요?", "견과류", [
        ("B", "Are you ready to order?", "주문하시겠어요?"),
        ("A", "Yes. I'll have the chicken salad.", "네. 치킨 샐러드 주세요."),
        ("B", "Would you like anything to drink?", "마실 건 필요하세요?"),
        ("A", "Just water, please. Does the salad have nuts?", "물만 주세요. 샐러드에 견과류 들어가요?"),
        ("B", "It does, but we can leave them out.", "들어가는데 빼 드릴 수 있어요."),
        ("A", "Please do. I'm allergic to nuts.", "그렇게 해 주세요. 견과류 알레르기가 있어요."),
    ]),
    ("여행", "Asking for Directions", "박물관까지 걸어서 얼마나 걸리나요?", "10분쯤", [
        ("A", "Excuse me. How do I get to the museum?", "실례합니다. 박물관에 어떻게 가요?"),
        ("B", "Go straight for two blocks and turn left.", "두 블록 직진한 다음 왼쪽으로 도세요."),
        ("A", "Is it far from here?", "여기서 멀어요?"),
        ("B", "Not really. It's about ten minutes on foot.", "별로요. 걸어서 10분쯤이에요."),
        ("A", "Thank you so much.", "정말 감사합니다."),
        ("B", "No problem. Enjoy your visit!", "천만에요. 즐거운 관람 되세요!"),
    ]),
    ("이야기", "The Brave Little Tent", "그날 밤 무엇이 불어왔나요?", "강한 바람", [
        ("", "There was a little yellow tent.", "작은 노란 텐트가 있었어요."),
        ("", "The other tents were big and strong.", "다른 텐트들은 크고 튼튼했어요."),
        ("", "One night, a strong wind came.", "어느 날 밤, 강한 바람이 불어왔어요."),
        ("", "The big tents shook, but the little tent held on.", "큰 텐트들은 흔들렸지만 작은 텐트는 꽉 버텼어요."),
        ("", "By morning, the whole family was sleeping inside it.", "아침이 되자 온 가족이 그 안에서 자고 있었어요."),
    ]),
    ("이야기", "The Missing Marshmallows", "마시멜로를 먹은 건 누구였나요?", "너구리", [
        ("", "Dad put a bag of marshmallows on the table.", "아빠가 마시멜로 한 봉지를 탁자에 두었어요."),
        ("", "When he came back, the bag was gone.", "돌아와 보니 봉지가 없어졌어요."),
        ("", "Mom looked at Dad. Dad looked at the kids.", "엄마는 아빠를, 아빠는 아이들을 쳐다봤어요."),
        ("", "Then they heard a sound behind the tent.", "그때 텐트 뒤에서 소리가 들렸어요."),
        ("", "A raccoon was eating their marshmallows!", "너구리가 마시멜로를 먹고 있었어요!"),
    ]),
    ("이야기", "Stars Over the Lake", "딸은 별을 몇 개까지 셌나요?", "100개", [
        ("", "After dinner, we lay down by the lake.", "저녁을 먹고 우리는 호숫가에 누웠어요."),
        ("", "The sky was full of stars.", "하늘에 별이 가득했어요."),
        ("", "My daughter started to count them.", "딸이 별을 세기 시작했어요."),
        ("", "She counted to one hundred and fell asleep.", "딸은 백까지 세고 잠들었어요."),
        ("", "I carried her to the tent and smiled.", "나는 딸을 텐트로 안고 가며 웃었어요."),
    ]),
    ("이야기", "The First Fish", "잡은 물고기는 어떻게 했나요?", "놓아주었어요", [
        ("", "Grandpa taught me how to fish.", "할아버지가 낚시하는 법을 가르쳐 주셨어요."),
        ("", "I waited for a long time, but nothing happened.", "오래 기다렸지만 아무 일도 없었어요."),
        ("", "Suddenly, my line moved.", "갑자기 낚싯줄이 움직였어요."),
        ("", "I pulled hard and caught a small silver fish.", "힘껏 당겨서 작은 은빛 물고기를 잡았어요."),
        ("", "We took a photo and let it go.", "우리는 사진을 찍고 물고기를 놓아주었어요."),
    ]),
    ("장비", "A Lantern for Every Trip", "한 번 충전하면 몇 시간 쓸 수 있나요?", "20시간쯤", [
        ("", "This is the lantern I take on every camping trip.", "이건 제가 캠핑 갈 때마다 챙기는 랜턴이에요."),
        ("", "It's small, but it's really bright.", "작지만 정말 밝아요."),
        ("", "On one charge, it lasts about twenty hours.", "한 번 충전하면 20시간쯤 가요."),
        ("", "You can also hang it from the top of your tent.", "텐트 천장에 걸 수도 있어요."),
        ("", "The only downside is that it gets a little warm.", "유일한 단점은 조금 따뜻해진다는 거예요."),
    ]),
    ("장비", "My Folding Chair", "의자 무게는 얼마인가요?", "1kg쯤", [
        ("", "Let me show you my favorite folding chair.", "제가 제일 좋아하는 접이식 의자를 보여 드릴게요."),
        ("", "It weighs about one kilogram.", "무게는 1kg쯤이에요."),
        ("", "It folds down to the size of a water bottle.", "접으면 물병만 한 크기가 돼요."),
        ("", "It takes less than a minute to set up.", "펴는 데 1분도 안 걸려요."),
        ("", "It's not cheap, but I use it every weekend.", "싸지는 않지만 주말마다 써요."),
    ]),
    ("장비", "Camp Stove Tips", "바람 부는 날에는 무엇을 쓰라고 했나요?", "바람막이", [
        ("", "Today I'll share three tips for using a camp stove.", "오늘은 캠핑 버너 쓰는 팁 세 가지를 알려 드릴게요."),
        ("", "First, always cook on a flat surface.", "첫째, 항상 평평한 곳에서 요리하세요."),
        ("", "Second, use a windscreen on windy days.", "둘째, 바람 부는 날에는 바람막이를 쓰세요."),
        ("", "Third, never use a stove inside your tent.", "셋째, 텐트 안에서는 절대 버너를 쓰지 마세요."),
        ("", "Stay safe and enjoy your meal.", "안전하게, 맛있게 드세요."),
    ]),
    ("장비", "Packing Light", "배낭 전체 무게는 몇 kg인가요?", "8kg", [
        ("", "People often ask me what's in my backpack.", "제 배낭에 뭐가 들었는지 자주 물어보세요."),
        ("", "The whole bag weighs only eight kilograms.", "가방 전체가 8kg밖에 안 돼요."),
        ("", "I bring one pot, one cup, and one spoon.", "냄비 하나, 컵 하나, 숟가락 하나만 가져가요."),
        ("", "My sleeping bag is the heaviest thing.", "침낭이 제일 무거워요."),
        ("", "Packing light makes the walk much more fun.", "짐을 가볍게 싸면 걷는 게 훨씬 즐거워요."),
    ]),
]

CATS = ["전체", "가족", "리액션", "일상", "여행", "캠핑", "편집", "유튜브"]
LCATS = ["전체", "여행", "이야기", "장비", "뉴스", "연설", "대화"]
