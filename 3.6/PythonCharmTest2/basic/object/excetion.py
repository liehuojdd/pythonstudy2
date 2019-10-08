from basic.object.student import student

if __name__=='__main__':
    try:
        student.mro1()
    #except Exception:
    except AttributeError:
    # AttributeError: type object 'student' has no attribute 'mro1'
        print('Catched exception')

    else:
        pass
    finally:
        print('Finally')