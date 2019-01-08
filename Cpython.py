# include <iostream>
# include <Python.h>
# include <numpy/arrayobject.h>

using namespace std;

void init_numpy(){
    import_array();
}

int main(){

    //Py_SetPythonHome(); 设置python的编译环境
    //python环境初始化
    Py_Initialize(); 
    if (Py_IsInitialized()){

        //导入sys模块
        PyRun_SimpleString("import sys\nsys.argv=['']");  
        PyRun_SimpleString("sys.path.append('/home/laibo/workspace/asq')"); // python文件路径

    }

    //使用numpy
    init_numpy(); 

    //导入需要调用的模块
    PyObject *pyModule = PyImport_ImportModule("invokepython"); 
    if (!pyModule) {
        printf("Can not open python module\n");
        return -1;
    }

    //获取python模块中相应的函数名
    PyObject *pyFunc = PyObject_GetAttrString(pyModule,"mmap_fvecs");
    PyObject *pyReturnValue;
    
    //参数
    PyObject *pyArg = Py_BuildValue("O&","filename");
    
    //调用函数，得到返回值
    pyReturnValue=PyObject_CallObject(pyFunc,pyArg);

    //关闭python解释器
    Py_Finalize();
    
}
