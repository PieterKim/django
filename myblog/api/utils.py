def obj_to_post(obj, flag=True):
    post = dict(vars(obj)) # obj들어오는 속성들을 dictionary 형태로 저장하겠다.

    if obj.category: # 값이 있으면
        post['category'] = obj.category.name
    else:
        post['category'] = "NoCategory"

    if obj.tags:
        post['tags'] = [t.name for t in obj.tags.all()]
    else:
        post['tags'] = []

    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = "https://via.placeholder.com/900x300/"

    if obj.update_date:
        post['update_date'] = obj.update_date.strftime('%Y-%m-%d %H:%M:%S')
    else:
        post['update_date'] = '9999-12-31 00:00:00'
    
    del post['_state'], post['category_id'], post['create_date']
    
    if not flag:
        del post['tags'], post['update_date'], post['description'], post['content']

    return post


def prev_next_post(obj):
    try:
        prevObj = obj.get_previous_by_update_date()
        prevDict = {
            'id' : prevObj.id,
            'title' : prevObj.title
        }
    except obj.DoesNotExist:
        prevDict = {}

    try:
        nextObj = obj.get_next_by_update_date()
        nextDict = {
            'id' : nextObj.id,
            'title' : nextObj.title
        }
    except obj.DoesNotExist:
        nextDict = {}
        
    return prevDict, nextDict