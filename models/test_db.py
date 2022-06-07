school = {
    'school_name': '',  # tên trường
    'level_count': '',  # cấp trường : vd tiểu học-1, trung học cơ sở-2, trung học phổ thông-3, đại học-4, học viện-4
    'school_type': '',  # loại trường : vd tiểu học, trung học cơ sở, vv
    'is_active': '',  # trạng thái
    'created_time': '',
    'updated_time': '',
}

user = {
    'user_id': '',  # id user: SV_01, GV_01, ADM_01, GĐ_01
    'position': '',  # chức vụ của user: admin, student, manager, teacher
    'full_name': '',  # tên đầy đủ: vd Nguyễn Bá Hải
    'major': '',  # Khoa : vd Công nghệ phần mềm, công nghệ thông tin
    'class': '',  # Lớp : vd Công nghệ phần mềm 1, công nghệ thông tin 2
    'study_time': '',  # thời gian học tập (chỉ dành cho student)
    'gender': '',  # giới tính
    'date_of_birth': '',  # ngày sinh
    'email': '',
    'phone': '',  # số điện thoại
    'school': school,  # thông tin trường học
    'is_active': '',  # trạng thái
    'created_time': '',
    'updated_time': '',
    'identity': '',  # chứng minh thư, căn cước công dân
    'signature': '',  # ảnh chữ kí (path)
}

diplomas = {
    'school': '',  # thông tin trường
    'major': '',  # Khoa : vd Công nghệ phần mềm, công nghệ thông tin
    'training_system': '',  # hệ đào tạo : vd cử nhân, kĩ sư, cao đẳng, trung cấp
    'user': user,  # thông tin user
    'awarded_place': '',  # nơi cấp bằng
    'awarded_date': '',  # ngày cấp bằng
    'degree_awarder': '',  # thông tin người cấp
    'id_graduate_certification': '',  # số hiệu bằng, mã bằng
    'graduate_certification_date': '',  # Ngày quyết định cấp bằng
    'signature': '',  # chữ kí
    'degree_image': '',  # ảnh bằng
}
