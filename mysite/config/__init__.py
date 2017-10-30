# 1. member application 생성
# 2. AbstractUser를 상속받은 User구현
#   User에 img_profile (ImageField)추가
# 3. AUTH_USER_MODEL = 'member.User'
# 4. settings.py의 INSTALLED_APPS에 'member'추가
# 5. member/admin.py에 User, UserAdmin을 사용