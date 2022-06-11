user = {
    'user_id': '',  # id user: SV_01, GV_01, ADM_01, GĐ_01
    # chức vụ của user: admin, student, manager, teacher
    'position': {
        'admin': '',
        'manager': '',
        'teacher': '',
        'student': ''
    },
    'full_name': '',  # tên đầy đủ: vd Nguyễn Bá Hải Bánh
    # Khoa : Công nghệ thông tin, Quản trị kinh doanh
    'department': {
        'department_name': '',
        # nghành học : Kỹ thuật phần mền, Hệ thống thông tin, Trí tuệ nhân tọa AI,An Toàn thông tin
        'major': {
            'major_name': '',
            # Lớp : vd Công nghệ phần mềm 1, công nghệ thông tin 2
            'class': {
                'class_name': '',
                'start-year': '',
                'graduate-year': '',
            },
        }
    },

    'study_time': '',  # thời gian học tập (chỉ dành cho student)
    'gender': '',  # giới tính
    'date_of_birth': '',  # ngày sinh
    'email': '',
    'phone': '',  # số điện thoại
    'school': '',  # thông tin trường học
    'is_active': '',  # trạng thái
    'created_time': '',
    'updated_time': '',
    'identity': '',  # chứng minh thư, căn cước công dân
    'id_school_year': '',  # niên khóa vd: k54 , k63 (cho sinh viên)
    'signature': '',  # ảnh chữ kí (path)
    'user_image': '',  # ảnh user (path)
}

school = {
    'school_id': '',  # mã trường vd HVKTQS
    'school_name': '',  # tên trường
    'level_count': '',  # cấp trường : vd tiểu học-1, trung học cơ sở-2, trung học phổ thông-3, đại học-4, học viện-4
    'school_type': '',  # loại trường : vd tiểu học, trung học cơ sở, vv
    'is_active': '',  # trạng thái
    'created_time': '',
    'updated_time': '',
}

diplomas = {
    'school': '',  # thông tin trường
    'major': '',  # Khoa : vd Công nghệ phần mềm, công nghệ thông tin
    'training_system': '',  # hệ đào tạo : vd cử nhân, kĩ sư, cao đẳng, trung cấp
    'graduation_grade': '',  # loại bằng : vd khá giỏi trung bình
    'user': '',  # thông tin user
    'awarded_place': '',  # nơi cấp bằng
    'awarded_date': '',  # ngày cấp bằng
    'degree_awarder': '',  # thông tin người cấp
    'id_graduate_certification': '',  # số hiệu bằng, mã bằng
    'graduate_certification_date': '',  # Ngày quyết định cấp bằng
    'signature': '',  # chữ kí
    'degree_image': '',  # ảnh bằng
}
