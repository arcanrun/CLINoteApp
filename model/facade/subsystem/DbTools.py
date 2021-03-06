from model.facade.interfaces.IDataBase import IDataBase
import shelve


class DBTools(IDataBase):
    def add(self, item):
        db = shelve.open('shelveDb')
        last_id = len(db.keys()) - 1
        if not last_id == -1:
            db[str(last_id + 1)] = item
        else:
            db['0'] = item
        db.close()

    def change_item(self, item, id):
        db = shelve.open('shelveDb')
        db[id] = item
        db.close()

    def get_all_items(self):
        all_data = []
        db = shelve.open('shelveDb')
        for k,v in db.items():
            all_data.append([k,v])
        return all_data

    def get_item(self, id):
        db = shelve.open('shelveDb')
        try:
            return db[str(id)]
        except KeyError:
            return None

    def delete_item(selfm, id):
        db = shelve.open('shelveDb')
        db.pop(str(id))
        db.close()

    def clear_db(self):
        db = shelve.open('shelveDb')
        db.clear()
        db.close()

    def get_items_by_date(self, date):
        res = []
        db = shelve.open('shelveDb')
        for k, v in db.items():
            if v.get_date() == date:
                res.append([k,v])
        return res

    def get_items_by_category(self, category):
        res = []
        db = shelve.open('shelveDb')
        for k, v in db.items():
            if v.get_category() == category:
                res.append([k,v])
        return res


